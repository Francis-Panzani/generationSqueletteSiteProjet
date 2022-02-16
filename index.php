<?php

function array_flatten($array) { 
    //si c'est pas un tableau on renvois rien
    if (!is_array($array)) { 
        return false; 
    }

    $result = array();

    foreach ($array as $key => $value) { 
        if (is_array($value)) { 
            //si on tombe sur une autre dimention on merge la dimention dans notre tableau results
            $result = array_merge($result, array_flatten($value)); 
        } else { 
            //si on tombe sur une simple value on la merge dans notre tableau values
            $result = array_merge($result, array($key => $value));
        } 
    }

    //on retourne notre tableau mis a plat
    return $result; 
}

//Exclu de la liste des fichiers a DL 

function list_file($ori_folder){
    //on scan le dossier courant
    $folder = scandir($ori_folder);

    //on supprime . et ..
    unset($folder[array_search('.', $folder, true)]);
    unset($folder[array_search('..', $folder, true)]);
    unset($folder[array_search('_exercice', $folder, true)]);
    unset($folder[array_search('_exercices', $folder, true)]);
    //on supprime les éléments indésirables
    foreach ($folder as $folder_value) {
        //on vire tous les fichiers qui commencent par un . (caché sous linux )
        if (substr($folder_value, 0, 1) === ".") {
            unset($folder[array_search($folder_value, $folder, true)]);
            continue;
        }
   //     echo $folder_value;
        // enlève tous les .php
        if (substr($folder_value, -4, 4) === ".php") {
            unset($folder[array_search($folder_value, $folder, true)]);
            continue;
        }
        
       //nom du fichier actuel et ceux qu'on souhaite exclure : 
        switch ($folder_value) {
             case pathinfo($_SERVER['PHP_SELF'], PATHINFO_BASENAME):
                 unset($folder[array_search($folder_value, $folder, true)]);
                 break;
                case '.html' :
                    unset($folder[array_search($folder_value, $folder, true)]);
                    break;
            default:
                # code...
                break;
        }

    }
  //  echo pathinfo($_SERVER['PHP_SELF'], PATHINFO_BASENAME);
 //   print_r($folder);

    //si le dossier est vide on retourne rien
    if (count($folder) < 1){
        return;
    }

    //on boucle sur tous les fichier du dossier
    foreach($folder as $folder_value){
        if(is_dir($ori_folder.'/'.$folder_value)) {
            //si on detecte un sous dossier on le repasse dans notre fonction list_file
            $folder_result = list_file($ori_folder.'/'.$folder_value);
        } else {
            //si c'est juste un fichier on le reformate avec le chemin exact
            $folder_result = $ori_folder.'/'.$folder_value;
        }
        //on stock dans un tableau chaque lien de fichier
        $result[] = $folder_result;
    }

    //je retourne a plat mon tableau de chemin de fichier pour faciliter l'affichage
    return array_flatten($result);
}

function download($nom, $situation, $poids)
{
    header('Content-Type: application/octet-stream');
    header('Content-Length: ' . $poids);
    header('Content-disposition: attachment; filename=' . $nom);
    header('Pragma: no-cache');
    header('Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0');
    header('Expires: 0');
    readfile($situation);
    exit();
}

if (isset($_POST['dl_button'])) {
    if (file_exists($_POST['dl_file'])) {
        download(basename($_POST['dl_file']) . PHP_EOL, $_POST['dl_file'], 10000);
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listing du dossier</title>
</head>
<body>
<ul>
<center><h1>Liste des fichiers contenus dans le dossier et ses sous-dossiers : </h1></center>

    <?php
    //je boucle sur les fichier des dossier et sous dossier de mon dossier courant
    foreach (list_file(getcwd()) as $value) {
        //je reformate ma value pour avoir uniquement le chemin partant du dossier courant et pas de la base de ma machine
        $value = str_replace(getcwd()."/", "", $value);
    ?>
    <li>
        <form method="POST">
            <?=$value;?> <a href="<?=$value;?>">Voir le fichier</a>
            <input type="hidden" name="dl_file" value="<?=$value;?>">
            <input type="submit" name="dl_button" value="Télécharger">
        </form>
    </li>
    <?php
    unset($value);
    }
    ?>
    <center>
    <h4>Merci de ne pas diffuser, © all rights reserved</h4></center>
</ul>
</body>
</html>