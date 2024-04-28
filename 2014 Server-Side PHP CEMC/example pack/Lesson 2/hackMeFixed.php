<!DOCTYPE html>
<!--
Example of what could happen if you don't clean up your user input. This
version is fixed.

Sam Scott, 2014
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <h1>Try to hack me by sending a parameter called "param" that contains a 
            &lt;script&gt; element. This version of the script is fixed so you 
            should not be able to hack the browser.</h1>
        <?php
        $safeString = trim($_GET["param"]);
        $safeString = stripslashes($safeString);
        $safeString = htmlspecialchars($safeString);
        echo "<p>$safeString</p>";
        ?>
    </body>
</html>
