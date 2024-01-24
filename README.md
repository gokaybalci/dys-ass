
<h1 align="center">
  <br>
  <a href="https://github.com/gokaybalci/dys-ass"><img src="dys-ass.png" alt="DYS Ass" width="200"></a>
  </h1>
  <div align="center">
<sup>(short for assistance)</sup> 
</div>




<h4 align="center">An assistance/accessibility tool for MEB's DYS built with PlayWright.</h4>

<p align="center">
<a href="https://saythanks.io/to/gokaybalci">
<img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
<a href="https://www.buymeacoffee.com/gokay" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="20" width="100"></a>
</p>

<p align="center">
  <a href="#key-features">Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>


## Key Features

* School Switch - Marks as read for every school you are registered as teacher
  - Goes through all DYS documents one by one.
* ~~GUI Login Mode for Windows users~~ *(soon)*


## How To Use

To clone and run this application, you'll need [Python](https://www.python.org/downloads/). From your command line:

```bash
# Clone this repository
git clone https://github.com/gokaybalci/dys-ass.git

# Go into the repository
cd dys-ass

# Install dependencies
pip install -r requirements.txt

# Write your e-Devlet login credentials into edevlet.txt (or creat edevlet.txt and then write them)

echo "TC Kimlik No" > edevlet.txt
echo "e-Devlet Şifresi" >> edevlet.txt

# Run the app
python3 main.py
```

> **Note**
> If you're using Windows, you can edit edevlet.txt file with Notepad. (*I will add more secure authentication methods in the future.*)


## Download

- I will add binaries to [Releases](https://github.com/gokaybalci/dys-ass/releases).


## Credits

This software uses the following open source packages:

- [PlayWright](https://playwright.dev/)


## License

GPL-3.0 license
