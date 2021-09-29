# app

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Performance diagnosis tips
```shell
# analyze the chunk-vendors.js and create a production build
npm run report  

# Generate performance report using LightHouse
lighthouse http://119.3.63.164/home --chrome-flags="--window-size=1920,1080" --view \
  --output-path performance_report/index.html  
```

### Serve the production build on server
```shell
npm install --global yarn
yarn global add serve
npx serve -s -l tcp://0.0.0.0:80 dist
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Try the hosted frontend
See [http://119.3.63.164/home](http://119.3.63.164/home).