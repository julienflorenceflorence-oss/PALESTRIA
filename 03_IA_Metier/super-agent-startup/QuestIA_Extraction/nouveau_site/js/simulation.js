/**
 * QuestIA - Simulation Engine
 * Handles dialogue branching, scoring, and HUD updates.
 */

class Simulation {
    constructor(missionData) {
        this.data = missionData;
        this.roundIdx = 0;
        this.stats = { ...missionData.start };
        this.history = [];
        
        // DOM Elements
        this.els = {
            speaker: document.getElementById('q-speaker'),
            line: document.getElementById('q-line'),
            choices: document.getElementById('q-choices'),
            confidence: document.getElementById('q-confidence'),
            stress: document.getElementById('q-stress'),
            score: document.getElementById('q-score'),
            roundProgress: document.getElementById('q-round-progress')
        };
        
        this.init();
    }

    init() {
        console.log(`Simulation started: ${this.data.title}`);
        this.renderStats();
        this.nextRound();
    }

    renderStats() {
        if (this.els.confidence) this.els.confidence.innerText = `${this.stats.confidence}%`;
        if (this.els.stress) this.els.stress.innerText = `${this.stats.stress}%`;
        
        // Calculate a global score based on metrics
        const globalScore = Math.round((this.stats.confidence + this.stats.fluency + this.stats.vocab + this.stats.structure) / 4);
        if (this.els.score) this.els.score.innerText = globalScore;
    }

    nextRound() {
        if (this.roundIdx >= this.data.rounds.length) {
            this.endSimulation();
            return;
        }

        const round = this.data.rounds[this.roundIdx];
        this.els.speaker.innerText = round.prompt.speaker;
        this.typeText(round.prompt.text);
        
        // Update Progress
        this.els.roundProgress.innerText = `ROUND ${this.roundIdx + 1} / ${this.data.rounds.length}`;
        
        this.renderChoices(round.options);
    }

    typeText(text) {
        this.els.line.innerHTML = "";
        let i = 0;
        const speed = 30;
        const type = () => {
            if (i < text.length) {
                this.els.line.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        };
        type();
    }

    renderChoices(options) {
        this.els.choices.innerHTML = "";
        options.forEach((opt, idx) => {
            const btn = document.createElement('button');
            btn.className = 'choice-btn';
            btn.innerHTML = `<span class="choice-key">${idx + 1}</span> ${opt.text}`;
            btn.onclick = () => this.selectChoice(opt);
            this.els.choices.appendChild(btn);
        });
    }

    selectChoice(option) {
        // Apply deltas
        for (let key in option.delta) {
            this.stats[key] = Math.max(0, Math.min(100, this.stats[key] + option.delta[key]));
        }
        
        this.renderStats();
        
        // Show reaction
        this.els.speaker.innerText = option.reaction.speaker;
        this.els.line.innerHTML = `<span class="reaction-text">${option.reaction.text}</span>`;
        this.els.choices.innerHTML = "";
        
        // Show Coach feedback after a small delay
        setTimeout(() => {
            const coachMsg = document.createElement('div');
            coachMsg.className = `coach-feedback feedback-${option.type}`;
            coachMsg.innerHTML = `<strong>COACH IA:</strong> ${option.coach}`;
            this.els.choices.appendChild(coachMsg);
            
            const nextBtn = document.createElement('button');
            nextBtn.className = 'btn btn-primary';
            nextBtn.style.marginTop = '20px';
            nextBtn.innerText = "Suivant →";
            nextBtn.onclick = () => {
                this.roundIdx++;
                this.nextRound();
            };
            this.els.choices.appendChild(nextBtn);
        }, 1000);
    }

    endSimulation() {
        this.els.speaker.innerText = "MISSION TERMINÉE";
        this.els.line.innerText = "Analyse de performance en cours...";
        this.els.choices.innerHTML = `<a href="../index.html" class="btn btn-primary">Retour au Hub</a>`;
        // Transition vers un écran de débriefing plus complet ici.
    }
}
