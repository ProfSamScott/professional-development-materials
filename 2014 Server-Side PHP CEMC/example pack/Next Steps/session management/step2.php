<?php
/*
 * These files show you how session management works. 
 * 
 * 1. Always start the session at the very top of your file. Otherwise you'll get an error.
 */
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Session Management</title>
    </head>
    <body>
        <?php
        // 2. Store data in the $_SESSION superglobal
        $_SESSION["name"] = $_GET["name"];
        ?>
        <h1>Hello <?= $_SESSION["name"] ?></h1>
        <p>How old are you?</p>
        <form action="step3.php" method="GET">
            <input type="number" name="age">
            <input type="submit">
        </form>
    </body> 
</html>
