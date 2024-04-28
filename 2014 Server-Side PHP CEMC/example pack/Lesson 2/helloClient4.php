<!DOCTYPE html>
<?php
/* Example Hello World program with Parameters. Same as HelloClient2.php but 
 * this one has as much interleaving of PHP and HTML as possible.
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
            ?>
            <p>Hello, Mr. <?= $_GET["lastName"] ?>.
                <?php
                if (isset($_GET["firstName"])) {
                    ?>
                    May I call you <?= $_GET["firstName"] ?>?
                    <?php
                }
                ?>
            </p>
            <?php
        } else {
            ?>
            <p>Hello. You forgot to specify your name.</p>
            <?php
        }
        ?>
    </body>
</html>
