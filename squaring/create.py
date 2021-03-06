b= '''

<!--Copyright 2020-2021 SUNIL KUMAR YADAV. (https://sunilkuyadav.github.io/MathFun/)-->
<!DOCTYPE html>
<html lang="">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="titlel"></title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="../cal.css">
    <script src="squaring.js"></script>
    <script defer src="cdown.js"></script>
</head>

<body>
    <div class="cantainer">
        <div class="main">
            <div class="operation">
                <nav class="navbar navbar-expand-md bg-dark navbar-dark">
                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                  <div class="collapse navbar-collapse" id="collapsibleNavbar">
                    <ul class="navbar-nav">
                      <li class="nav-item">
                        <a class="nav-link sp" href="../addition.html">Addition</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link sp" href="../substraction.html">Substraction</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link sp" href="../multiplication.html">Multiplication</a>
                      </li> 
                      <li class="nav-item">
                        <a class="nav-link sp" href="../division.html">Division</a>
                      </li>
                        <li class="nav-item">
                        <a class="nav-link sp" href="../tablefun.html">TableFun</a>
                      </li>
                        <li class="nav-item">
                        <a class="nav-link sp" href="../squaring.html">Squaring</a> 
                        </li>
                    </ul>
                  </div>  
                </nav>
            </div>
            <div class="mul">
            <div class="dropdown">
                <button type="button" class="btn dropdown-toggle btnl" data-toggle="dropdown">Level |
    </button>
                <div id="qs" class="qs"></div>
                    <div class="text-center dropdown-menu">
                        <a id="l1" onclick="squ(1,1,20,0,0)" class="dropdown-item l_s" href="l1.html">Level 1</a>
                        <a id="l2" onclick="squ(2,21,40,0,0)" class="dropdown-item l_s" href="l2.html">Level 2</a>
                        <a id="l3" onclick="squ(3,41,60,0,0)" class="dropdown-item l_s" href="l3.html">Level 3</a>
                        <a id="l4" onclick="squ(4,61,80,0,0)" class="dropdown-item l_s" href="l4.html">Level 4</a>
                        <a id="l5" onclick="squ(5,81,99,0,0)" class="dropdown-item l_s" href="l5.html">Level 5</a>
                        <a id="l6" onclick="squ(6,1,99,0,0)" class="dropdown-item l_s" href="l6.html">Level 6</a>
                        <a id="l7" onclick="squ(7,100,200,0,0)" class="dropdown-item l_s" href="l7.html">Level 7</a>
                        <a id="l8" onclick="squ(8,200,300,0,0)" class="dropdown-item l_s" href="l8.html">Level 8</a>
                        <a id="l9" onclick="squ(9,300,400,0,0)" class="dropdown-item l_s" href="l9.html">Level 9</a>
                        <a id="l10" onclick="squ(10,400,500,0,0)" class="dropdown-item l_s" href="l10.html">Level 10</a>
                        <a id="l11" onclick="squ(11,500,600,0,0)" class="dropdown-item l_s" href="l11.html">Level 11</a>
                        <a id="l12" onclick="squ(12,600,700,0,0)" class="dropdown-item l_s" href="l12.html">Level 12</a>
                        <a id="l13" onclick="squ(13,700,800,0,0)" class="dropdown-item l_s" href="l13.html">Level 13</a>
                        <a id="l14" onclick="squ(14,800,900,0,0)" class="dropdown-item l_s" href="l14.html">Level 14</a>
                        <a id="l15" onclick="squ(15,900,999,0,0)" class="dropdown-item l_s" href="l15.html">Level 15</a>
                        <a id="l16" onclick="squ(16,100,999,0,0)" class="dropdown-item l_s" href="l16.html">Level 16</a>
                        <!--<a id="l17" onclick="squ(17,1000,1100)" class="dropdown-item l_s" href="l17.html">Level 17</a>
                        <a id="l18" onclick="squ(18,1100,1200)" class="dropdown-item l_s" href="l18.html">Level 18</a>
                        <a id="l19" onclick="squ(19,1200,1300)" class="dropdown-item l_s" href="l19.html">Level 19</a>
                        <a id="l20" onclick="squ(20,1300,3000)" class="dropdown-item l_s" href="l20.html">Level 20</a>
                        <a id="l21" onclick="squ(21,3000,5000)" class="dropdown-item l_s" href="l21.html">Level 21</a>
                        <a id="l22" onclick="squ(22,5000,9999)" class="dropdown-item l_s" href="l22.html">Level 22</a>-->
                    </div>
                </div>
                <div id="quest">
                    <div class="question" id="question">start</div>
                    <div id="cd"><div id="app"></div></div>
                </div>
                <hr>
                <div class="input">
                    <div id="option-buttons" class="btn-grid">
                        <button id="btn1" class="btn btnc" href="">1</button>
                        <button id="btn2" class="btn btnc" href="#">2</button>
                        <button id="btn3" class="btn btnc" href="#">3</button>
                        <button id="btn4" class="btn btnc" href="#">4</button>
                    </div>
                </div>
                <hr>
                <div class="hint">
                    <button id="hintshow" class="hintshow btn" type="button">HINT</button>
                    <h1 id="hint">Squaring</h1>
                </div>
            </div>        
            
        </div>
    </div>
    <footer>
            <div class="cpd">SUNIL KUMAR YADAV &copy; 2020-21</div>
    </footer>
</body>
        <script>
            $( document ).ready(function() {
        $('#l|').click();
    });
        $('.l_s').on('click',function(){
            $('.btnl').text(($(this).text()));
            $('#titlel').text(($(this).text())+" Squaring");
        });
    </script>
</html>

'''
for i in range(2,23):
    x = b.replace('|',str(i))
    p = ('l'+str(i)+'.html')
    f = open(p,"w")
    f.write(x)
    f.close()
    
