<!DOCTYPE html>
<?php
/* Example Hello World program with Parameters
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
        echo "<p>Hello, Mr. {$_GET["lastName"]}. May I call you {$_GET["firstName"]}?</p>";
        ?>
    </body>
</html>
