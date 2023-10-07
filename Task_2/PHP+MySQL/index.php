<?php
session_start();
if(!isset($_SESSION['username'])) {
    header('Location: login.php');
    exit();
}
?>

<!doctype html>
<html lang="en">

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

<body>
    <nav class="navbar navbar-light justify-content-center fs-3 mb-5 text-white fw-bold" style="background-color: cadetblue">
        Task 2
    </nav>

    <div class="container">
        <?php
        if (isset($_GET['msg'])) {
            $msg = $_GET['msg'];
            echo '<div class="alert alert-warning alert-dismissible fade show" role="alert">
                ' . $msg . '
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>';
        }
        ?>
        <!-- tìm kiếm -->
        <div>
            <form action="index.php" class="d-flex p-3" method="post">
                <label for="username" class="fw-bold d-flex justify-content-center align-items-center m-2 ">Search:</label>
                <input class="form-control me-2" id="username" type="search" name="username" placeholder="Search by username" aria-label="Search">
                <button class="btn btn-outline-primary" name="search" type="submit">Search</button>
            </form>
        </div>

        <table class="table table-hover text-center">
            <thead class="table-dark">
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Userame</th>
                    <th scope="col">Address</th>
                    <th scope="col">Phone Number</th>
                </tr>
            </thead>

            <tbody>
                <?php
                $conn = mysqli_connect("localhost", "root", "", "task_2");
                if (!$conn) {
                    echo "<script type='text/javascript'>alert('Connection failed!');</script>";
                }                                       
                if (isset($_POST['search'])) {
                    $username = $_POST['username'];

                    $sql = "SELECT * FROM task_2 WHERE username = '$username'";
                    $result = mysqli_query($conn, $sql);
                    while ($rows = mysqli_fetch_assoc($result)) {
                ?>
                        <tr>
                            <td><?php echo $rows['id'] ?></td>
                            <td><?php echo $rows['username'] ?></td>
                            <td><?php echo $rows['address'] ?></td>
                            <td><?php echo $rows['phonenumber'] ?></td>
                        </tr>
                <?php 
                    }
                    if (mysqli_num_rows($result) == 0) {
                        echo "<script type='text/javascript'>alert('Username does not exist!');</script>";
                    }
                }
                ?>

            </tbody>
        </table>

        <div class="d-flex justify-content-center">
            <a href="logout.php" class="btn btn-danger mb-3">Log out</a>
        </div>

    </div>
    <!-- bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>

</html>
