# Painel — Jornada rumo à medalha (OBMEP 2026)

Painel de acompanhamento do lançamento da trilha OBMEP 2026 (2ª fase, rede
municipal), publicado como página estática via GitHub Pages.

## Como funciona

- A planilha de gestão (abas Painel / Checklist / Acesso) é buscada **direto
  do Google Sheets** a cada execução (precisa estar compartilhada como
  "Qualquer pessoa com o link — Leitor"). O link/ID fica em `GOOGLE_SHEET_ID`
  no topo de `build_data.py`.
- Um export de gamificação (`gamificacao.csv`) — esse continua sendo por
  arquivo mesmo, exportado manualmente do LMS.
- `build_data.py` gera:
  - `data.json` — dados agregados (público, vai para o site). **Não contém
    nome de aluno**, apenas números por turma/município.
  - `interno/gamificacao_detalhado.csv` — lista por aluno, para conferência
    interna. Este arquivo é ignorado pelo git (`.gitignore`) e nunca deve ser
    publicado.
  - `index.html` — a página do painel, gerada a partir de `index.template.html`
    com os dados embutidos.

## Para atualizar o painel com novos dados

1. Edite a planilha de gestão direto no Google Sheets normalmente — não
   precisa exportar nem baixar nada.
2. Salve o novo CSV de gamificação (ex: na pasta Downloads).
3. Rode:

   ```bash
   python build_data.py
   ```

   (sem argumentos — a planilha vem do Google Sheets e o CSV usa o último
   caminho configurado em `CSV_PADRAO`, no topo do arquivo). Para usar um
   arquivo de planilha local em vez do Google Sheets, passe o caminho como
   primeiro argumento: `python build_data.py "caminho\planilha.xlsx" "caminho\gamificacao.csv"`.
4. Confira o resultado abrindo `index.html` no navegador.
5. Envie as mudanças pro GitHub (`git add`, `git commit`, `git push`) — a
   página publicada atualiza sozinha em 1-2 minutos.

## Acesso

Sem login por enquanto (decisão de simplificar) — quem tiver o link do GitHub
Pages acessa direto. Se um dia for preciso restringir por domínio de e-mail,
dá pra reaproveitar a ideia de "Entrar com Google" restrito a
`@associacaocactus.com.br`, mas isso fica para depois.

## Estrutura

```
build_data.py          -> script que gera data.json e index.html
index.template.html    -> layout/design do painel (editar aqui, não no index.html)
index.html             -> gerado automaticamente - não editar à mão
data.json              -> dados agregados públicos, gerado automaticamente
interno/               -> dados com nome de aluno, NÃO commitado (uso interno)
```
