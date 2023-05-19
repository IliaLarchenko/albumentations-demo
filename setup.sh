mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"ilia.larchenko@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
enableXsrfProtection=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
