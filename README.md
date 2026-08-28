# Painel — Jornada rumo à medalha (OBMEP 2026)

Painel de acompanhamento do lançamento da trilha OBMEP 2026 (2ª fase, rede
municipal), publicado como página estática via GitHub Pages.

## Como funciona

- `2026_Acompanhamento_JornadaOBMEP.xlsx` (abas Painel / Checklist / Acesso) e
  um export de gamificação (`gamificacao.csv`) são processados por
  `build_data.py`.
- `build_data.py` gera:
  - `data.json` — dados agregados (público, vai para o site). **Não contém
    nome de aluno**, apenas números por turma/município.
  - `interno/gamificacao_detalhado.csv` — lista por aluno, para conferência
    interna. Este arquivo é ignorado pelo git (`.gitignore`) e nunca deve ser
    publicado.
  - `index.html` — a página do painel, gerada a partir de `index.template.html`
    com os dados embutidos.

## Para atualizar o painel com novos dados

1. Salve a nova planilha e o novo CSV de gamificação (ex: na pasta Downloads).
2. Rode:

   ```bash
   python build_data.py "caminho\da\planilha.xlsx" "caminho\do\gamificacao.csv"
   ```

   Sem argumentos, o script usa os últimos caminhos de `Downloads` configurados
   no topo do arquivo (`XLSX_PADRAO` / `CSV_PADRAO`).
3. Confira o resultado abrindo `index.html` no navegador.
4. Envie as mudanças pro GitHub (`git add`, `git commit`, `git push`) — a
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
