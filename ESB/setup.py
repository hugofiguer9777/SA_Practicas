from distutils.core import setup 
import py2exe 
 
setup(name="esb", 
 version="1.0.0", 
 description="API para el ESB", 
 author="Hugo Figueroa", 
 author_email="hugofiguer97@gmail.com", 
 url="https://github.com/hugofiguer9777/SA_Practicas", 
 license="GLP", 
 scripts=["app.py"], 
 console=["app.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)