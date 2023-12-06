# Plantilla para proyectos Cookiecutter | Data Science

En este repositorio encontrarás una **plantilla** para tus proyectos de data science que desees crear en tu camino de aprendizaje y profesional, con ayuda de Cookiecutter

## Requerimientos

- Anaconda >= 4.x
- git >= 2.x
- Cookiecutter Python package >= 1.4.0:

Puedes instalar cookiecutter de las sigueintes dos maneras, dependiendo cual sea tu entorno preferido para usar Python [**pip** o **conda**]
- pip:  

```
pip install cookiecutter
```

- conda: 

```
conda install -c conda-forge cookiecutter
```

## Distribución de directorios
```

├── README.md
├── cookiecutter.json
├── environment.yaml
├── hooks
│   └── post_gen_project.py
└── {{ cookiecutter.project_slug }}
    ├── LICENCE
    ├── README.md
    ├── data
    │   ├── 0_external
    │   ├── 0_raw
    │   ├── 1_intermediate
    │   └── 2_processed
    ├── docs
    ├── environment.yaml
    ├── notebooks
    │   └── 0.0-{{ cookiecutter.project_slug }}-introduction.ipynb
    ├── reports
    ├── requirements.txt
    ├── scripts
    ├── setup.py
    └── {{ cookiecutter.project_slug }}_packages
        ├── __init__.py
        ├── utils
        │   ├── __init__.py
        │   └── get_path.py
        └── visualization
            ├── __init__.py
            └── visualization.py
```
## Sincronización

Para poder instalar esto en tu ámbito local debes hacer lo siguiente:

- En tu terminal, ubicarte en el area de trabajo donde deseas crear tu proyecto
- Posterior a esto escribir en tu linea de comandos lo siguiente
  
```
cookiecutter https://github.com/sebastianlopezacero/cookiecutter_personal
```
