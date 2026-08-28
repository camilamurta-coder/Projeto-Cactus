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

## Login por domínio (associacaocactus.com.br)

O painel fica atrás de uma tela de login com "Entrar com Google", restrita a
e-mails `@associacaocactus.com.br`. Importante: como o site é 100% estático
(GitHub Pages), essa tela **impede acesso casual** (quem não tem conta Google
da Cactus não entra), mas **não é segurança real** contra alguém tecnicamente
capaz de inspecionar o código-fonte do navegador — os dados agregados
(`data.json`) já estão embutidos no HTML entregue ao navegador antes do login
ser conferido.

Para ativar, é preciso criar um "OAuth Client ID" gratuito no Google Cloud
(vinculado à conta Google Workspace da Cactus):

1. Acesse <https://console.cloud.google.com/> logada com uma conta
   `@associacaocactus.com.br`.
2. Crie um projeto novo (ex: "Painel Cactus").
3. Menu lateral → **APIs e serviços** → **Tela de consentimento OAuth**.
   - Tipo de usuário: **Interno** (assim só contas do domínio conseguem
     logar — essa parte É imposta pelo próprio Google, de verdade).
   - Preencha nome do app e e-mail de suporte, salve.
4. Menu lateral → **APIs e serviços** → **Credenciais** → **Criar
   credenciais** → **ID do cliente OAuth**.
   - Tipo de aplicativo: **Aplicativo da Web**.
   - Em "Origens JavaScript autorizadas", adicione a URL do GitHub Pages
     (ex: `https://seu-usuario.github.io`).
   - Clique em Criar. Copie o **Client ID** gerado (termina em
     `.apps.googleusercontent.com` — não tem "segredo", pode ficar público).
5. Cole esse Client ID na constante `GOOGLE_CLIENT_ID` no topo do `<script>`
   em `index.template.html`, rode `python build_data.py` de novo e publique.

## Estrutura

```
build_data.py          -> script que gera data.json e index.html
index.template.html    -> layout/design do painel (editar aqui, não no index.html)
index.html             -> gerado automaticamente - não editar à mão
data.json              -> dados agregados públicos, gerado automaticamente
interno/               -> dados com nome de aluno, NÃO commitado (uso interno)
```
