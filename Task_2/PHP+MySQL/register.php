<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Task 2</title>
    <link rel="icon" type="image/x-icon" href="https://scontent.fhan14-3.fna.fbcdn.net/v/t39.30808-6/300582505_457118323100327_5264492577895373431_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=qMYwYD25960AX9qi2s9&_nc_ht=scontent.fhan14-3.fna&oh=00_AfCjRuo9eOURQuGdCT0ZcrZBVaqyG0e9HjQUhKU42JAFbg&oe=63E767A5">

    <!-- bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

    <!-- font awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<center>

    <body>
        <nav class="navbar navbar-light justify-content-center fs-3 mb-5 text-white fw-bold" style="background-color: cadetblue">
            REGISTER
        </nav>
        <form action="register.php" method="post" id="form" onsubmit="return validate()">
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" size="55"></td>
                </tr>
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" size="55"></td>
                </tr>
                <tr>
                    <td>Repassword: </td>
                    <td><input type="password" name="repassword" size="55"></td>
                </tr>
                <tr>
                    <td>Address: </td>
                    <td><input type="text" name="address" size="55"></td>
                </tr>
                <tr>
                    <td>Phone Number: </td>
                    <td><input type="text" name="phonenumber" size="55"></td>
                </tr>
                <tr style="text-align: right;">
                    <div class="px-5 my-4 d-flex justify-content-center">
                        <td><button type="submit" name="login" class="btn btn-primary ">Login</button></td>
                        <td><button type="submit" name="register" class="btn btn-primary">Register</button></td>
                    </div>
                </tr>
            </table>
        </form>
        <?php
        session_start();
        $conn = mysqli_connect("localhost", "root", "", "task_2");
        if (isset($_POST['register']) && $_POST['username'] != '' && $_POST['password'] != '' && $_POST['repassword'] != '' && $_POST['address'] != '' && $_POST['phonenumber'] != '') {
            $username = $_POST['username'];
            $password = $_POST["password"];
            $repassword = $_POST["repassword"];
            $address = $_POST["address"];
            $phonenumber = $_POST["phonenumber"];
            
            $sql = "SELECT * FROM task_2 WHERE username ='$username' ";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_assoc($result);

            if ($row != 0) {
                echo "<script type='text/javascript'>alert('Username already exists!');</script>";
            } else if ($password != $repassword) {
                echo "<script type='text/javascript'>alert('Repassword does not match');</script>";
            } else {
                $password = md5($password);
                $sql = "INSERT INTO task_2 (username, password, address, phonenumber) VALUES ('$username','$password','$address','$phonenumber') ";
                $result  = mysqli_query($conn, $sql);
                if ($result) {
                    echo "<script type='text/javascript'>alert('Register successed');</script>";
                } else {
                    echo "Failed: " . mysqli_error($conn);
                }
            }
        }
        if (isset($_POST['login'])) {
            header('location: login.php');
        }

        ?>
    </body>
</center>

</html>
