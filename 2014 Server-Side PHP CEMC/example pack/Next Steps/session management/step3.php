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
        $_SESSION["age"] = $_GET["age"];
        ?>
        <h1>Hello <?= $_SESSION["name"] ?></h1>
        <p>What's your favorite color?</p>
        <form action="step4.php" method="GET">
            <input type="color" name="color">
            <input type="submit">
        </form>
    </body>
</html>
