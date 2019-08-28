# Introduction to git

Live slides available at [cis-ncbj.github.io/git-introduction](http://cis-ncbj.github.io/git-introduction).

The slide deck contains a basic introduction for Git.

## slides
For the slides we use the [RevealJS](https://github.com/hakimel/reveal.js/) framework.
- See index.html for the slide show composition
- See markdown/* for the slide sources.

### Run the slides from sources
- You can also run the slides locally in a container from sources.
```
docker run -d -p 80:80 --name slides \
  -v ${PWD}:/usr/share/nginx/html nginx
```
- Or use docker-compose to avoid some issues with nginx when running docker in a VM using boot2docker
```
docker-compose up -d
```
- Open a browser [slides](http://localhost/)
