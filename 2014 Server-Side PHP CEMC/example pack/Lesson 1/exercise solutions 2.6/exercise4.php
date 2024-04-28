<!DOCTYPE html>
<!--
Counting exercise solution.
Sam Scott, 2014
-->
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
    <body>
        <?php
        $start = 2;
        $end = 10000;
        for ($i = $start; $i <= $end; $i+=1)
            if ($i % 2 == 0)
                echo "<p>$i</p>";
        ?>
    </body>
</html>
