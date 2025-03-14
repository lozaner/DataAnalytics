En este proyecto iniciamos haciendo la primera aplicacion Web en la pagina de render en la cual notaremos una grafica y empezare a hacer una aplicacion web de todo mi portafolio y dejare ya dos link en este proyecto, tuve unos problemas para cargar de Visual Studio Code a GitHub el codigo que me arrojaba fue 

RPC failed; HTTP 400 curl 22 The requested URL returned error: 400 Bad Request

y al parecer fue porque modifique el repositorio que descargue con nuevos archivos y de esta forma fue obligado a cargar y funciono

y se resolvio poniendo los siguientes lineas de codigos 

git config http.postBuffer 524288000 
git push --force origin 
git push --all

despues el problema fue quue este proyecto lo quise hacer dentro del repositorio de mis proyectos porque decian que debian estar guardados en ciertas carpetas los archivos como el de streamlit y el de EDA en notbook y sin embarga jamaz me cargo me dijo el maestro que creara un nuevo repositorio solo para estoy asi lo hice cualquier duda o comentario estoy abierto a sugerencias erick no ira guiando como cargar nuetra web de nustros repositorios y pues en esto estoy subiendo mis proyectos a GitHub

[Ver Proyecto](https://notebooks-o54z.onrender.com)