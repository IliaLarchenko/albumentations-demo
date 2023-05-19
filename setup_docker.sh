mkdir -p ~/.streamlit/

echo -e "\
[server]\n\
headless = true\n\
enableCORS=false\n\
enableXsrfProtection=false\n\
" > ~/.streamlit/config.toml
