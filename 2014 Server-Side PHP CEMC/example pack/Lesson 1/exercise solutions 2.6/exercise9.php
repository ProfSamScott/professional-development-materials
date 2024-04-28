<!DOCTYPE html>
<!--
Solution to slot machine exercise
Sam Scott, 2014
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Sam's Slots!</title>
        <style type="text/css">
            img {
                width:50px;
                height:50px;
            }
            td {
                border:3px solid black;
                padding:10px;
                width:50px;
                height:50px;
                text-align:center;
                font-family:sans-serif;
                font-size:24px;
            }
            td#spin {
                padding:0px;
                background-color:rgb(128,0,0);
            }
            input[type=submit] {
                width:70px;
                height:70px;
                border:none;
                background-color:rgb(128,0,0);
                margin:0px;
                color:white;
                font-weight:bold;
                font-size:24px;
            }
            input[type=number] {
                width:50px;
                text-align:right;
            }
            h1 {
                color:rgb(128,0,0);
                font-size:50px;
                margin-bottom:5px;
            }
            h1,h2 {
                font-family:sans-serif;
            }
            h2 {
                color:rgb(0,128,0);
            }
            body {
                text-align:center;
            }
            table {
                margin:auto;
            }
        </style>
    </head>
    <body>
        <?php
        $f1 = rand(1, 7);
        $f2 = rand(1, 7);
        $f3 = rand(1, 7);
        if ($f1 == $f2 && $f2 == $f3)
            $win = 10;
        elseif ($f1 == $f2 || $f2 == $f3 || $f3 == $f1)
            $win = 2;
        else
            $win = 0;
        ?>
        <h1>Sam's Slots!</h1>
        <form action="exercise9.php" method="GET">
            <table>
                <tr>
                    <td><img src="fruit/<?= $f1 ?>.png"></td>
                    <td><img src="fruit/<?= $f2 ?>.png"></td>
                    <td><img src="fruit/<?= $f3 ?>.png"></td>
                    <td id='spin'><input type="submit" value="SPIN"></td>
                </tr>
            </table>
        </form>
        <?php
        if ($win == 2)
            echo "<h2>Win!</h2>";
        elseif ($win == 10)
            echo "<h2>Jackpot!</h2>";
        elseif ($win == 0)
            echo "<p>Sorry you lose.</p>";
        ?>
    </body>
</html>
