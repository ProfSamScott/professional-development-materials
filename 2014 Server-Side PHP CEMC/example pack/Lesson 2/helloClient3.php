<!DOCTYPE html>
<?php
/* Example Hello World program with Parameters. Same as helloClient2.php
 * but with more interleaving of HTML and PHP
 * 
 * Sam Scott, March 2012
 */
?>
<html>
    <head>
        <meta charset='UTF-8'>
        <title>Hello Client</title>
    </head>
    <body>
        <?php
        if (isset($_GET["lastName"])) {
            echo "<p>Hello, Mr. {$_GET["lastName"]}.";
            if (isset($_GET["firstName"]))
                echo "May I call you {$_GET["firstName"]}?</p>";
            else
                echo "</p>";
        } else {
            ?>
            <p>Hello. You forgot to specify your name.</p>
            <?php
        }
        ?>
    </body>
</html>
