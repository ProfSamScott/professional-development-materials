<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        $_SESSION["color"] = $_GET["color"];
        ?>
        <h1>Hello</h1>
        <p>Here's what I know about you...</p>
        <ul>
            <li>Your name is <?= $_SESSION["name"] ?></li>
            <li>You are <?= $_SESSION["age"] ?> years old</li>
            <li>Your favorite color is 
                <span style='color:<?= $_SESSION["color"] ?>'>
                    This one!
                </span> 
            </li>
        </ul>
        <p>I shall now forget everything...</p>
        <?php
        session_destroy();
        ?>
    </body>
</html>
