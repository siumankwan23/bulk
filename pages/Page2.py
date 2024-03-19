import re
import streamlit as st

def extract_urls_from_text(text):
    # Use regex to find URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    # Filter URLs to keep only those ending with "_zpid/" and remove duplicates
    filtered_urls = list(set(url for url in urls if url.endswith("_zpid/")))

    # Print the filtered URLs
    if filtered_urls:
        st.success("Filtered URLs:")
        for url in filtered_urls:
            st.write(url)
        
        # Export filtered URLs to link.txt
        with open('link.txt', 'w') as output_file:
            for i, url in enumerate(filtered_urls):
                if i < len(filtered_urls) - 1:
                    output_file.write(f'"{url}",\n')
                else:
                    output_file.write(f'"{url}"\n')
        st.info("Exported filtered URLs to link.txt")
    else:
        st.warning("No unique URLs ending with '_zpid/' found in the text.")

# Streamlit UI
st.title("URL Extractor from Text")
text_input = st.text_area("Enter the text:", "Paste your text here...")
if st.button("Extract URLs"):
    extract_urls_from_text(text_input)