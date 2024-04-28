<!DOCTYPE html>
<!--
Counting exercise solution. 
Sam Scott, 2014
-->
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Counting</title>
    </head>
    <body>
        <?php
        if (isset($_GET["start"])) {
            $start = $_GET["start"];
        } else {
            $start = 1;
        }
        if (isset($_GET["end"])) {
            $end = $_GET["end"];
        } else {
            $end = 1000;
        }
        if (isset($_GET["by"])) {
            $by = $_GET["by"];
        } else {
            $by = 1;
        }
        for ($i = $start; $i <= $end; $i+=$by)
            echo "<p>$i</p>";
        ?>
    </body>
</html>
