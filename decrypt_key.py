<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Harmless Download</title>
</head>
<body>

    <a id="downloadLink" href="harmless.py" download="harlmless.py" style="display: none;"></a>

    <h1>Harmless</h1>
    <p>Silakan klik tombol di bawah ini untuk memulai unduhan file Anda.</p>
    
    <button id="startButton">Mulai Unduhan Sekarang</button>
    
    <p id="message" style="color: green; display: none;">Unduhan dimulai...</p>

    <script>
        document.addEventListener('DOMContentLoaded', (event) => {
            const downloadLink = document.getElementById('downloadLink');
            const startButton = document.getElementById('startButton');
            const message = document.getElementById('message');

            if (startButton && downloadLink) {
                // Tambahkan event listener untuk merespons KLIK pengguna
                startButton.addEventListener('click', () => {
                    // 1. Tampilkan pesan
                    message.style.display = 'block';
                    
                    // 2. Sembunyikan tombol
                    startButton.style.display = 'none';
                    
                    // 3. Panggil metode .click() pada tautan tersembunyi
                    //    Ini berfungsi karena dipicu langsung dari klik pengguna
                    downloadLink.click();
                    
                    // Opsional: Alihkan pengguna setelah beberapa detik jika unduhan gagal terdeteksi
                    // setTimeout(() => {
                    //     // Lakukan sesuatu, misalnya tampilkan pesan manual
                    // }, 5000); 
                });
            }
        });
    </script>

</body>
</html>
