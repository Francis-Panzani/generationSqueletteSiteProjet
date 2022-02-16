import csv
from distutils.dir_util import copy_tree
import shutil
import os
if os.path.exists('preproduction'):
 shutil.rmtree('preproduction') # vire le contenu du dossier preproduction
if not os.path.exists('preproduction'):
 os.makedirs('preproduction')

fromDirectory = "arborescence_base"
toDirectory = "preproduction"
#on copie l'arbo des dossiers
copy_tree(fromDirectory, toDirectory)

liste_lien_index=""
liste_area="""<img src="images/cecisoweb-sitemap-V0.3.2.png" alt="sitemap" usemap="#image-map" class="map">\n
<map name="image-map">\n"""
with open('areamap.csv',encoding="ISO-8859-1", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
            numero=row[0]
            nom_page=row[1]
            chemin=row[2]
            coords=row[3]
            shape=row[4]
            target=row[5]
            partie=row[6]
            version=row[7]
            chem_img_maq=row[8]
            image_maquette=row[9]
            definition_of_done=row[10]
            couleur_de_fond=row[11]
            liste_lien_index+="""<br><a href="/preproduction/%s%s.html">Aller a&#768; la page %s - %s</a>"""% (chemin,nom_page,numero,nom_page)
            liste_area+="""<area target="%s" title="%s %s - v %s" href="%s%s.html" coords="%s" shape="%s" id="num%s" data-maphilight='{"stroke":false,"fillColor":"%s","fillOpacity":0.3,"alwaysOn":true}'>\n"""% (target,numero,nom_page,version,chemin,nom_page,coords,shape,numero,couleur_de_fond)
            texte = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="ISO-8859-1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cecisoweb - %s</title>
    <style>
        h1{
            text-align: center;
            }
        h2,h3,h4,h5{
            text-align: center;
            text-decoration: underline;
        }
    </style>

</head>
<body>
    <h1> %s - %s - Version %s</h1>
    <a href="/preproduction/index.html">Retour a&#768; l'index </a>
    """% (nom_page,numero,nom_page,version)
            if not chem_img_maq:
                texte +="""
                <hr>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.<br><br> Fugiat voluptatibus eligendi fuga magnam.<br> Blanditiis fuga fugit maiores natus aspernatur architecto porro doloremque quis voluptate doloribus.<br> Sequi culpa quod numquam natus.<br>
                <hr>
                """
            else:
                texte +="""<hr> <h3>Maquette  </h3> 
                <img src="/preproduction/%s%s" alt="%s" >\n
                <hr>"""% (chem_img_maq,image_maquette,image_maquette)
            if definition_of_done:    
             texte +="""
              <h3>Done : </h3>
              <br>%s
              """% (definition_of_done)
            else :

             texte +="""
            <h3>Done : </h3>
     
    <ol>
        <li> Un lien / icone redirigera vers la homepage </li>
        <li> Un bouton back to top ramenera tout en haut de la page, qui apparaitra si la page fait plus de la taille de l'e&#769;cran  </li>
        <li> </li>
        <li> </li>
        <li> </li>
        <li> </li>
        <li> </li>
        <li> </li>   
            </ol>
        </body>
        </html>""" 
            x=open('preproduction/'+chemin+nom_page+'.html','w')
            x.write(texte)
            x.close()
liste_area+="</map>"
numero=0
nom_page='index'
chemin=''
texte = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="ISO-8859-1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cecisoweb - Index </title>
    <style>
        h1,h2,h3,h4,h5{
            text-align: center;
            text-decoration: underline;
        }
    </style>
   
        <script type="text/javascript" src="/preproduction/js/jquery-3.3.1.min.js"></script>
    <script type="text/javascript" src="/preproduction/js/jquery.maphilight.js"></script>
     <link href="/preproduction/css/stylenav.css" rel="stylesheet">
     <script type="text/javascript" src="/preproduction/js/stickytop.js"></script>
    <script type="text/javascript">
		$(function() {
		$('.map').maphilight();
        });
    </script>
</head>
<body>
   <!-- https://codepen.io/_codemics/pen/PwEbYJ -->


    <div class="nav">

        <div class="topcoat-button-bar">
            <div class="topcoat-button-bar__item ">
              <button class="topcoat-button-bar__button bleu">V0.2.4</button>
            </div>
            <div class="topcoat-button-bar__item">
              <button class="topcoat-button-bar__button rouge">V0.2.5</button>
            </div>
            <div class="topcoat-button-bar__item">
              <button class="topcoat-button-bar__button vert">V0.2.6</button>
            </div>
         </div>
 </div>  
    <h1> %s - Index  </h1>
    <a href="/preproduction/vue/Homepage.html">Retour a&#768; la Homepage </a>
    %s
    <h2>Sommaire et liste des pages : </h2>
    %s
    <hr>
Lorem ipsum dolor sit amet consectetur adipisicing elit.<br><br> Fugiat voluptatibus eligendi fuga magnam.<br> Blanditiis fuga fugit maiores natus aspernatur architecto porro doloremque quis voluptate doloribus.<br> Sequi culpa quod numquam natus.<br>

    <hr>
    <h3>Done : </h3>
     
    <ol>
        <li> Un bouton back to top ramenera tout en haut de la page, qui apparaitra si la page fait plus de la taille de l'e&#769;cran  </li>
        <li> </li>
        <li> </li>
        <li> </li>
        <li> </li>
        <li> </li>
        <li> </li>   

    </ol>
</body>
</html>""" % (numero,liste_area,liste_lien_index)
x=open('preproduction/'+chemin+nom_page+'.html','w')
x.write(texte)
x.close() 




