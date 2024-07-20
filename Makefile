STREAMLIT_APP := "main.py"
FASTAPI_APP := "main.py"

run_app: # make run
	cd app && streamlit run $(STREAMLIT_APP)

# documentation at http://localhost:8000/docs
run_api: # access the api at http://localhost:8000  (note use http not https)
	cd api && fastapi run $(FASTAPI_APP)
