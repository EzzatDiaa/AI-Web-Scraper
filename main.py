import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama
st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")

if st.button("Scrape Size"):
    st.write("Scraping...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    clean_body_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_body_content

    with st.expander("view DOM Content"):
        st.text_area("DOM Content", clean_body_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing...")

            dom_chunks =    split_dom_content(st.session_state.dom_content)
            parsed_results = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_results)