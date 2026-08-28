#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escreve o export de gamificacao (CSV por aluno) numa aba do Google Sheets
da planilha de gestao, usando uma conta de servico do Google.

Uso:
    python sync_gamificacao.py [caminho_csv]

Requer (ver README.md, secao "Escrever no Google Sheets"):
    - pip install gspread google-auth (ja instalado neste projeto)
    - SERVICE_ACCOUNT_JSON abaixo apontando para o arquivo de credencial
      baixado do Google Cloud Console
    - a planilha compartilhada com o e-mail dessa conta de servico, como
      Editor
"""

from __future__ import annotations

import sys
from pathlib import Path

import gspread

from build_data import CSV_PADRAO, GOOGLE_SHEET_ID, ler_gamificacao

# Caminho do arquivo JSON da conta de servico. NUNCA commitar este arquivo -
# ele fica fora do repositorio (pasta secrets/, ja no .gitignore).
SERVICE_ACCOUNT_JSON = str(Path(__file__).parent / "secrets" / "painel-cactus-service-account.json")

ABA_GAMIFICACAO = "Gamificação"


def main() -> int:
    if not SERVICE_ACCOUNT_JSON:
        print("! SERVICE_ACCOUNT_JSON nao configurado - edite sync_gamificacao.py "
              "com o caminho do arquivo .json da conta de servico")
        return 1

    caminho_json = Path(SERVICE_ACCOUNT_JSON)
    if not caminho_json.exists():
        print(f"! arquivo de credencial nao encontrado: {caminho_json}")
        return 1

    caminho_csv = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(CSV_PADRAO)
    if not caminho_csv.exists():
        print(f"! csv nao encontrado: {caminho_csv}")
        return 1

    alunos = ler_gamificacao(caminho_csv)

    linhas = [["Turma", "Aluno", "Nível", "Pontos", "Conquistas"]]
    for a in alunos:
        linhas.append([a["turma"], a["aluno"], a["nivel"], a["pontos"], a["conquistas"]])

    gc = gspread.service_account(filename=str(caminho_json))
    sh = gc.open_by_key(GOOGLE_SHEET_ID)

    try:
        ws = sh.worksheet(ABA_GAMIFICACAO)
        ws.clear()
    except gspread.WorksheetNotFound:
        ws = sh.add_worksheet(title=ABA_GAMIFICACAO, rows=len(linhas) + 10, cols=6)

    ws.update(linhas, "A1")
    print(f"{len(alunos)} estudantes escritos na aba '{ABA_GAMIFICACAO}' do Google Sheets "
          f"(dados com nome - a aba precisa da planilha estar com acesso restrito, "
          f"nao publica).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
