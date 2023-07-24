.PHONY: sanity_tests_headless_report sanity_tests_report sanity_tests api_tests_report api_tests

sanity_tests_headless_report:
	export HEADLESS=true
	pytest tests/sanity_tests/test_sanity.py --datafile=tests/test_data/test_data.json --html=reports/sanity_tests_report.html --self-contained-html

sanity_tests_report:
	export HEADLESS=false
	pytest tests/sanity_tests/test_sanity.py --datafile=tests/test_data/test_data.json --html=reports/sanity_tests_report.html --self-contained-html

sanity_tests:
	export HEADLESS=false
	pytest tests/sanity_tests/test_sanity.py --datafile=tests/test_data/test_data.json

api_tests_report:
	pytest tests/api_tests/test_api.py --datafile=tests/test_data/test_data.json --html=reports/api_tests_report.html --self-contained-html

api_tests:
	pytest tests/api_tests/test_api.py --datafile=tests/test_data/test_data.json
