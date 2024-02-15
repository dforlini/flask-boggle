$(document).ready(function(){
    let score = 0;
    let timeLeft = 60;
    let timerInterval;

    function startTimer() {
        timerInterval = setInterval(function(){
            if (timeLeft > 0){
                timeLeft--;
                $('#time').text(timeLeft);
            }else{
                clearInterval(timerInterval);
                endGame();
            }
        }, 1000)
    }

    function endGame() {
        $('#guessForm input[type="submit').prop('disabled', true);
        $('#reshuffleButton').prop('disabled', true);
        $('#feedback').text("Time is up! Final score:" +score);
    }
    
    function resetGame() {
        score = 0;
        timeLeft = 60;
        $('#score').text(`Score: ${score}`);
        $('#time').text(timeLeft);
        $('#feedback').text('');
        $('#guessForm input[type="submit]').prop('disabled', false);
        $('#reshuffleButton').prop('disabled', false);
        reshuffleBoard();
        startTimer();
    }





    function reshuffleBoard(){
        axios.get('/reshuffle')
        .then(function(response){
            const board = response.data.board;
            let boardHtml = '';
            for (let row of board){
                boardHtml += '<tr>';
                for(let letter of row){
                    boardHtml += `<td>${letter}</td>`;
                }
                boardHtml += '</tr>';
            }
            $('table').html(boardHtml);
            score = 0;
            $('#score').text(`Score: ${score}`);
        })
        .catch(function(error){
            console.log(error);
        });
    }
    $('#newGameButton').click(function(){
        resetGame();
    });

    $('#guessForm').submit(function(event){
        event.preventDefault();
        let word = $('#guess').val();
        axios.post('/guess', { guess: word})
          .then(function(response){
            const { result, message } = response.data;
            $('#feedback').text(message);
    
            if (result === "ok"){
                const wordScore = word.length;
                score += wordScore;
                $('#score').text(`Score: ${score}`);
            }
          })
          .catch(function (error){
            console.log(error);
          });
        });
        $('#reshuffleButton').click(function(){
            reshuffleBoard();
        });
    });

