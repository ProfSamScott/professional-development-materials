<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
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
        if (!isset($_POST["bet"])) {
            $name = "";
            $bet = "1";
            $credit = "100";
            $f1 = $f2 = $f3 = 1;
            $win = -1;
        } else {
            $name = $_POST["name"];
            $credit = $_POST["credit"];
            $bet = $_POST["bet"];
            $f1 = rand(1, 7);
            $f2 = rand(1, 7);
            $f3 = rand(1, 7);
            if ($f1 == $f2 && $f2 == $f3)
                $win = 10;
            elseif ($f1 == $f2 || $f2 == $f3 || $f3 == $f1)
                $win = 2;
            else
                $win = 0;
            $credit -= $bet;
            $credit += $bet * $win;
        }
        ?>
        <h1>Sam's Slots!</h1>
        <form action="exercise5.php" method="POST">
            <table>
                <tr>
                    <td><img src="fruit/<?= $f1 ?>.png"></td>
                    <td><img src="fruit/<?= $f2 ?>.png"></td>
                    <td><img src="fruit/<?= $f3 ?>.png"></td>
                    <td id='spin'><input type="submit" value="SPIN"></td>
                </tr>
                <tr>
                    <td colspan='4'>
                        Name: <input type='text' required name='name' value='<?= $name ?>'>
                    </td>
                </tr>
                <tr>
                    <td colspan='4'>
                        Bet: <input type='number' required name='bet' value='<?= $bet ?>' min='1' max='<?= $credit ?>'>
                        Credit: <input type='number' required name='credit' value='<?= $credit ?>' readonly='true'>
                    </td>
                </tr>
            </table>
        </form>
        <?php
        if ($win == 2)
            echo "<h2>Win! $" . $win * $bet . "</h2>";
        elseif ($win == 10)
            echo "<h2>Jackpot! $" . $win * $bet . "</h2>";
        elseif ($win == 0)
            echo "<p>Sorry you lose.</p>";
        ?>
    </body>
</html>
