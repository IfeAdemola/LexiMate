STREAMLIT_APP := "main.py"

run: # make run
	cd app && streamlit run $(STREAMLIT_APP)
