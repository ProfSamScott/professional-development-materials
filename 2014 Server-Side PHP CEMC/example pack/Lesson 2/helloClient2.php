<!DOCTYPE html>
<?php
/* Example Hello World program with Parameters. This one handles the error
 * case more gracefully
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
        } else
            echo "<p>Hello. You forgot to specify your name.</p>";
            ?>
    </body>
</html>
