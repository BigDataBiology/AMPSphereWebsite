# AMPSphere website

###### tags: `AMPSphere`

<img src="https://github.com/BigDataBiology/AMPSphereWebsite/blob/main/frontend/src/assets/logo.png" style="height: 30px; width: 30px" /> ![](https://img.shields.io/badge/status-beta-yellow?style=flat-square&logo=appveyor) [![](https://img.shields.io/badge/DOI-10.5281/zenodo.4574468-brightgreen?style=flat-square&logo=appveyor)](https://doi.org/10.5281/zenodo.4574468)

Welcome to the AMPSphere website!


- Live website: http://ampsphere.big-data-biology.org/home.
- Backend API: http://ampsphere-api.big-data-biology.org/


## Dependencies

- For the backend
    - [Sqlite database](https://www.sqlite.org/index.html) -- data management
    - [FastAPI](https://fastapi.tiangolo.com/) -- backend API implementation
    - [Sqlalchemy](https://www.sqlalchemy.org/) -- database mapping and data querying
    - [Pydantic](https://pydantic-docs.helpmanual.io/) -- API data validation
    - [MMseqs](https://github.com/soedinglab/MMseqs2) -- AMP search API
    - [HMMER](http://hmmer.org/) -- family search API
    - [Gunicorn](https://gunicorn.org/) + [Uvicorn](https://www.uvicorn.org/) -- running the backend
    - [Nginx](https://www.nginx.com/) -- running as an intermediate server
- For the frontend
    - Vue.js ecosystems
        - [VueRouter](https://router.vuejs.org/) -- router across website pages
        - [VueAxios](https://www.npmjs.com/package/vue-axios) -- data access from the backend
        - [Quasar](https://quasar.dev/) + [Element Plus](https://element-plus.org/) -- building the website layout
    - [Plotly.js](https://plotly.com/javascript/) -- generating visualizations of data distribution
    - [LogoJS](https://logojs.wenglab.org/app/) -- generating Sequence logos for AMP families
    - [helicalwheel](https://github.com/clemlab/helicalwheel) -- generating helical wheel graphs for AMPs

## Issue reporting
The website is currently a work-in-progress, not yet ready for production. Any comments/feedback will be greatly appreciated. 

We receive feedback via [GitHub issues](https://github.com/BigDataBiology/AMPSphereWebsite/issues) and [Email](#Authors), but please first consider using the [GitHub issues](https://github.com/BigDataBiology/AMPSphereWebsite/issues), as the problem you're facing may be also useful to other users.

## Authors

|   Name    | Email                 | Organization                                                 |
| :-------: | --------------------- | ------------------------------------------------------------ |
| Hui Chong | hui@big-data-biology.org | Research Assistant, Institute of Science and Technology for Brain-inspired Intelligence, Fudan University |
| Célio Dias Santos Júnior | celio@big-data-biology.org | Postdoc Researcher, Institute of Science and Technology for Brain-inspired Intelligence, Fudan University |
| Luis Pedro Coelho | luispedro@big-data-biology.org  | Principle Investigator, Institute of Science and Technology for Brain-inspired Intelligence, Fudan University |

