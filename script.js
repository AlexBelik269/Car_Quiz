document.addEventListener('DOMContentLoaded', () => {
    let currentQuestionIndex = 0;
    let questions = [];
    let score = 0;
    const totalQuestions = 20;
    let selectedOption = null;
  
    async function fetchQuestions() {
        const difficulty = localStorage.getItem('difficulty');
        try {
            const response = await fetch(`http://localhost:5000/questions?difficulty=${difficulty}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            questions = data;
            showQuestion();
        } catch (error) {
            console.error('Fetch error:', error);
        }
    }
  
    function showQuestion() {
        if (currentQuestionIndex < totalQuestions) {
            const questionObj = questions[currentQuestionIndex];
            document.querySelector('.question_counter').innerText = `Question: ${currentQuestionIndex + 1}`;
            document.querySelector('.que_text').innerHTML = `<span>${questionObj.question}</span>`;
            document.querySelector('.option_list').innerHTML = questionObj.options.map((option, index) => `
                <div class="option" data-option="${String.fromCharCode(97 + index)}">
                    ${option}
                </div>
            `).join('');
  
            document.querySelectorAll('.option').forEach(option => {
                option.addEventListener('click', selectOption);
            });
  
            selectedOption = null;
            document.querySelector('.next_btn').disabled = true;
        } else {
            showResults();
        }
    }
  
    function selectOption(event) {
        if (selectedOption) return; // Prevent selecting another option
  
        selectedOption = event.target;
        const selectedAnswer = selectedOption.getAttribute('data-option');
        const correctAnswer = questions[currentQuestionIndex].correct_answer;
  
        if (selectedAnswer === correctAnswer) {
            selectedOption.classList.add('correct');
            score++;
        } else {
            selectedOption.classList.add('incorrect');
            document.querySelector(`.option[data-option="${correctAnswer}"]`).classList.add('correct');
        }
  
        document.querySelectorAll('.option').forEach(option => {
            option.removeEventListener('click', selectOption);
        });
  
        document.querySelector('.total_points span p').innerText = `${score} / ${totalQuestions} points`;
        document.querySelector('.next_btn').disabled = false;
    }
  
    function showResults() {
        const overlay = document.querySelector('.overlay');
        overlay.style.display = 'flex';
        overlay.querySelector('.score_text').innerHTML = `<b>CONGRATULATION!</b><br>You got ${score} out of ${totalQuestions} Points!`;

        if (score > 10) {
            const duration = 15 * 1000,
                  animationEnd = Date.now() + duration,
                  defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

            function randomInRange(min, max) {
                return Math.random() * (max - min) + min;
            }

            const interval = setInterval(function() {
                const timeLeft = animationEnd - Date.now();

                if (timeLeft <= 0) {
                    return clearInterval(interval);
                }

                const particleCount = 50 * (timeLeft / duration);

                // since particles fall down, start a bit higher than random
                confetti(
                    Object.assign({}, defaults, {
                        particleCount,
                        origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
                    })
                );
                confetti(
                    Object.assign({}, defaults, {
                        particleCount,
                        origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
                    })
                );
            }, 250);

            // Play the success song
            const audio = document.getElementById('song');
            audio.play();
        }

        document.querySelector('.result_box').style.display = 'none';
        overlay.querySelector('.restart').addEventListener('click', restartQuiz);
        overlay.querySelector('.quit').addEventListener('click', quitQuiz);
    }
  
    function restartQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        document.querySelector('.overlay').style.display = 'none';
        document.querySelector('.result_box').style.display = 'none';
        document.querySelector('.restart').style.display = 'none';
        document.querySelector('.quit').style.display = 'none';
        fetchQuestions();
    }
  
    function quitQuiz() {
        localStorage.removeItem('difficulty');
        window.location.href = 'home.html';
    }
  
    document.querySelector('.next_btn').addEventListener('click', () => {
        if (currentQuestionIndex < totalQuestions) {
            currentQuestionIndex++;
            showQuestion();
        }
    });
  
    fetchQuestions();
});
