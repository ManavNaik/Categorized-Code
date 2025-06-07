const questions = [
    {
      type: "single",
      question: "What is the capital of France?",
      answers: ["Berlin", "Madrid", "Paris", "Rome"],
      correct: [2]
    },
    {
      type: "single",
      question: "Which planet is known as the Red Planet?",
      answers: ["Earth", "Mars", "Jupiter", "Saturn"],
      correct: [1]
    },
    {
      type: "multi",
      question: "Which of these are programming languages? (Select all that apply)",
      answers: ["Python", "HTML", "CSS", "JavaScript"],
      correct: [0,3]
    },
    {
      type: "multi",
      question: "Select all prime numbers:",
      answers: ["2", "3", "4", "5"],
      correct: [0,1,3]
    }
  ];
  
  let currentQuestion = 0;
  let score = 0;
  
  const quizDiv = document.getElementById('quiz');
  const restartBtn = document.getElementById('restart');
  
  function arraysEqual(a, b) {
    return a.length === b.length && a.every((val, idx) => val === b[idx]);
  }
  
  function showQuestion() {
    const q = questions[currentQuestion];
    quizDiv.innerHTML = `
      <div class="question">
        Q${currentQuestion + 1} of ${questions.length}: ${q.question}
      </div>
      <form id="quiz-form">
        <div class="answers">
          ${q.answers.map((answer, i) => `
            <label class="input-label">
              <input type="${q.type === 'single' ? 'radio' : 'checkbox'}" name="option" value="${i}">
              ${answer}
            </label>
          `).join('')}
        </div>
        <button type="submit" class="submit-btn">Submit Answer</button>
      </form>
    `;
  
    document.getElementById('quiz-form').onsubmit = function(e) {
      e.preventDefault();
      let selected = [];
      const options = document.getElementsByName('option');
      options.forEach(opt => {
        if ((q.type === 'single' && opt.checked) || (q.type === 'multi' && opt.checked)) {
          selected.push(parseInt(opt.value));
        }
      });
      selected.sort((a, b) => a - b);
      const correct = [...q.correct].sort((a, b) => a - b);
      let isCorrect = arraysEqual(selected, correct);
      if (isCorrect) score++;
      currentQuestion++;
      if (currentQuestion < questions.length) {
        showQuestion();
      } else {
        showResult();
      }
    }
  }
  
  function showResult() {
    quizDiv.innerHTML = `
      <div class="question">
        Quiz completed!<br><br>Your score: <strong>${score} / ${questions.length}</strong>
      </div>
    `;
    restartBtn.style.display = 'inline-block';
  }
  
  restartBtn.onclick = () => {
    currentQuestion = 0;
    score = 0;
    restartBtn.style.display = 'none';
    showQuestion();
  }
  
  showQuestion();
  