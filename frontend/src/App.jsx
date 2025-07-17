import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [form, setForm] = useState({
    email: '',
    credit_score: '',
    income: '',
    family_background: 'Single',
    age_group: '18–25',
    comments: '',
    consent: false
  });
  const [leads, setLeads] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!form.consent) return alert("Please consent to data processing.");

    const response = await axios.post('https://your-fastapi-url/score', form);
    setLeads([...leads, response.data]);
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Lead Scoring Dashboard</h1>
      <form onSubmit={handleSubmit} className="grid gap-2">
        <input type="email" placeholder="Email" onChange={(e) => setForm({...form, email: e.target.value})} required />
        <input type="number" placeholder="Credit Score" onChange={(e) => setForm({...form, credit_score: e.target.value})} required />
        <input type="number" placeholder="Income" onChange={(e) => setForm({...form, income: e.target.value})} required />
        <select onChange={(e) => setForm({...form, family_background: e.target.value})}>
          <option>Single</option><option>Married</option><option>Married with Kids</option>
        </select>
        <select onChange={(e) => setForm({...form, age_group: e.target.value})}>
          <option>18–25</option><option>26–35</option><option>36–50</option><option>51+</option>
        </select>
        <textarea placeholder="Comments" onChange={(e) => setForm({...form, comments: e.target.value})}></textarea>
        <label>
          <input type="checkbox" onChange={(e) => setForm({...form, consent: e.target.checked})} /> I consent to data processing
        </label>
        <button type="submit">Submit</button>
      </form>
      <table className="mt-6 w-full border">
        <thead><tr><th>Email</th><th>Initial</th><th>Final</th><th>Comments</th></tr></thead>
        <tbody>
          {leads.map((l, idx) => (
            <tr key={idx}>
              <td>{l.email}</td><td>{l.initial_score}</td><td>{l.reranked_score}</td><td>{l.comments}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;