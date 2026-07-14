(function () {
    'use strict';

    var KNOWLEDGE = [
        { keys: ['hello', 'hi', 'hey'], answer: "Hello! I'm the HealingTech Initiative assistant. Ask me about our mission, programmes, partnership with HealingTech Labs, volunteering, or how to get involved." },
        { keys: ['healingtech labs', 'labs', 'powered', 'company', 'partner'], answer: "**HealingTech Labs** was born out of HealingTech Initiative — creating employment pathways and earning opportunities for the youth we train, including space for some to develop products of their own. Labs operates independently while collaborating through technology expertise and strategic support. [Learn more](https://healing-tech-customer-requiremnts-p.vercel.app/)" },
        { keys: ['initiative', 'what is', 'about', 'who are you'], answer: "**HealingTech Initiative** is a technology-driven social impact organization combining technology, AI, education, digital skills, innovation, inclusive support, healthcare access, community empowerment, and social innovation — with counselling and mental health support for people navigating difficult circumstances." },
        { keys: ['mission'], answer: "Our **mission** is to leverage technology to improve lives by fostering healing, empowering communities, and expanding access to education, healthcare, inclusive support and economic opportunities for youth and children while bridging the digital gap." },
        { keys: ['vision'], answer: "Our **vision** is creating a world where technology serves as a bridge to healing, empowerment, and sustainable opportunities for youth and children in adversity." },
        { keys: ['focus', 'programs', 'what do you do'], answer: "Our **focus areas** include technology, AI, education, digital skills, innovation, inclusive support, healthcare access, community empowerment, social innovation, and counselling support. Visit our **Initiatives** page for programmes like Future Coders and AI for Malawi." },
        { keys: ['volunteer', 'join'], answer: "We welcome volunteers — students, professionals, educators, designers, and developers. Visit our **Volunteer** page to apply or email **info@healingtechinitiative.org**." },
        { keys: ['partner', 'donate', 'support'], answer: "You can **partner** with us, **donate** to expand technology education, or **support our mission** to advance inclusion and opportunity across Africa. Visit Partners or Donate pages for details." },
        { keys: ['contact', 'email'], answer: "Contact us at **info@healingtechinitiative.org** or **+265 997 774 972**. Offices in Lilongwe, Malawi and Nairobi, Kenya. Visit our Contact page." },
        { keys: ['malawi', 'africa', 'kenya'], answer: "We operate across **Malawi and Kenya**, with a bold vision to expand inclusive digital opportunities throughout **Africa**." },
        { keys: ['support empower elevate', 'slogan'], answer: "Our motto is **Support · Empower · Elevate** — leveraging technology to improve lives and create pathways to resilience and success." }
    ];

    var DEFAULT = "I don't have confirmed information on that. Please contact **info@healingtechinitiative.org** or visit our Contact page.";

    var messagesEl, inputEl, sendBtn, chatHistory = [];

    function init() {
        messagesEl = document.getElementById('aiMessages');
        inputEl = document.getElementById('aiInput');
        sendBtn = document.getElementById('aiSend');
        if (!messagesEl) return;
        sendBtn.addEventListener('click', sendMessage);
        inputEl.addEventListener('keydown', function (e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } });
        addBotMessage("Hello! I'm the HealingTech Initiative assistant. Ask about our mission, vision, programmes, HealingTech Labs, volunteering, or partnerships.", true);
    }

    function findAnswer(text) {
        var lower = text.toLowerCase(), best = null, score = 0;
        KNOWLEDGE.forEach(function (k) { k.keys.forEach(function (key) { if (lower.indexOf(key) !== -1 && key.length > score) { score = key.length; best = k.answer; } }); });
        return best || DEFAULT;
    }

    function fmt(t) { return t.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br>'); }
    function esc(t) { var d = document.createElement('div'); d.textContent = t; return d.innerHTML; }

    function appendMessage(role, text) {
        var w = document.createElement('div'); w.className = 'ai-msg ' + role;
        var b = document.createElement('div'); b.className = 'ai-msg-bubble';
        b.innerHTML = role === 'bot' ? fmt(text) : esc(text);
        w.appendChild(b); messagesEl.appendChild(w); messagesEl.scrollTop = messagesEl.scrollHeight;
        chatHistory.push({ role: role, text: text });
    }

    function typeBotMessage(text) {
        var typing = document.createElement('div'); typing.className = 'ai-msg bot';
        typing.innerHTML = '<div class="ai-typing"><span></span><span></span><span></span></div>';
        messagesEl.appendChild(typing); messagesEl.scrollTop = messagesEl.scrollHeight;
        setTimeout(function () {
            typing.remove();
            var w = document.createElement('div'); w.className = 'ai-msg bot';
            var b = document.createElement('div'); b.className = 'ai-msg-bubble'; w.appendChild(b); messagesEl.appendChild(w);
            var parts = text.split(/(\s+)/), i = 0, cur = '';
            (function next() {
                if (i < parts.length) { cur += parts[i]; b.innerHTML = fmt(cur); messagesEl.scrollTop = messagesEl.scrollHeight; i++; setTimeout(next, 28); }
                else chatHistory.push({ role: 'bot', text: text });
            })();
        }, 700);
    }

    function addBotMessage(text, instant) { if (instant) appendMessage('bot', text); else typeBotMessage(text); }

    function sendMessage() {
        var text = inputEl.value.trim(); if (!text) return;
        appendMessage('user', text); inputEl.value = ''; sendBtn.disabled = true;
        setTimeout(function () { typeBotMessage(findAnswer(text)); sendBtn.disabled = false; inputEl.focus(); }, 300);
    }

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
