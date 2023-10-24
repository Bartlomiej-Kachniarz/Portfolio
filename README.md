# Portfolio
## This is my Machine Learning projects portfolio

Here you can find my projects ranging from pure python coding to advanced Machine Learning projects.

The repository shall be extended to contain Data Engineering as well as DevOps projects.

In case of any questions please contact me:

- [LinkedIn](https://www.linkedin.com/in/bart%C5%82omiej-kachniarz-5208b8153/)
- [e-mail](bart.kach@gmail.com)

### The repository structure is displayed below:

```bash
.
├── data_engineering
│   └── airflow
│       ├── dags
│       │   └── process-employees.py
│       ├── airflow.cfg
│       ├── airflow.sh
│       ├── docker-compose.yaml
│       ├── install_airflow.sh
│       └── webserver_config.py
├── machine_learning
│   ├── meteorite_landings
│   │   └── meteorite_landings_analysis.ipynb
│   ├── mnist
│   │   └── mnist_digits.ipynb
│   ├── msl-images
│   │   └── README.md
│   ├── mushrooms_dataset
│   │   ├── README.md
│   │   └── mushrooms.ipynb
│   ├── sentiment_analysis
│   │   ├── hugging_face.ipynb
│   │   └── nltk.ipynb
│   ├── xgboost
│   │   └── first_xgboost.ipynb
│   └── youtube_llm
│       └── youtube_llm.ipynb
├── python
│   ├── design_patterns
│   │   ├── abstract_factory
│   │   │   └── car_app.py
│   │   └── factory_method
│   │       ├── logistics_app.py
│   │       └── shipments.py
│   ├── dto
│   │   └── game_character.ipynb
│   ├── games_in_python
│   │   ├── connectfour.py
│   │   ├── snake.py
│   │   └── tetris.py
│   ├── training
│   │   ├── matplotlib.ipynb
│   │   ├── numpy.ipynb
│   │   └── pandas.ipynb
│   └── web_scraping_projects
│       ├── books_to_scrape
│       │   └── books_to_scrape
│       │       └── spiders
│       │           └── books2scrape.py
│       ├── ebay
│       │   └── ebay
│       │       ├── spiders
│       │       │   └── ebay_books.py
│       │       └── books.json
│       ├── glasses
│       │   ├── glasses
│       │   │   └── spiders
│       │   │       └── glasses_shop.py
│       │   └── glasses.json
│       ├── imdb
│       │   └── imdb
│       │       └── spiders
│       │           ├── rating_10k.py
│       │           └── top_imdb_movies.py
│       ├── livecoin
│       │   └── livecoin
│       │       └── spiders
│       │           └── coin.py
│       ├── national_debt
│       │   └── national_debt
│       │       └── spiders
│       │           └── gdp_debt.py
│       ├── quotes
│       │   └── quotes
│       │       └── spiders
│       │           └── quotess.py
│       └── worldometers
│           └── worldometers
│               ├── spiders
│               │   └── countries.py
│               ├── runner.py
│               └── runner_2.py
├── .gitignore
├── .pre-commit-config.yaml
├── .pylintrc
├── .pyproject.toml
├── LICENSE.txt
├── README.md
├── requirements.txt
├── setup.cfg
└── setup.py
``````

<!-- create the new tree by running: -->
<!-- tree . -I '__pycache__|mlruns|__init__.py|.DS_Store|venv/|.git/|.metals/|.vscode/|.ipynb_checkpoints|*.csv|*.shp|*.shx|*.dbf|*.prj|*.bin|.scala-build|*.npy|*.npz|*ubyte|*ed.txt|*.Z|cardiffnlp|data.txt|index.txt|tetrisscores.txt|agaricus-lepiota.txt|items.py|middlewares.py|pipelines.py|settings.py|scrapy.cfg|example*|*.out|*.sql' --dirsfirst -a --gitignore --prune -->