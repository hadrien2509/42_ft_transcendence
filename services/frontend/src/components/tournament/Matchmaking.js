import React, { useState } from 'react';
import { useUsers } from './UserContext';
import { useLocation } from 'react-router';
import ProfilePic from '../user/getProfilePic';
import Game from '../game/game'; // Import the Game component
import ThreejsGame from '../game/threejs';
import Morpion from '../morpion/morpion';
const backendHost = 'http://' + window.location.hostname + ':8000';

const Matchmaking = () => {
  const { users, setUsers } = useUsers();
  const [participants, setParticipants] = useState(users);
  const [currentMatch, setCurrentMatch] = useState(null);
  const [currentPair, setCurrentPair] = useState(0);

  const location = useLocation();
  const game = location.state?.game;

  const doTournament = (event) => {
    event.preventDefault();

    if (participants.length < 2) {
      alert('Tournament is over!');
      return;
    }

    let player1;
    let player2;
  
    if (!participants[currentPair]) {
      setCurrentPair(0);
      player1 = participants[0];
    }
    else {
      player1 = participants[currentPair];
    }

    if (!participants[currentPair + 1]) {
      setCurrentPair(0);
      player2 = participants[1];
    }
    else {
      player2 = participants[currentPair + 1];
    }

    setCurrentPair(currentPair + 1);
    setCurrentMatch({ player1, player2 });
  };

  const fetchMatchResult = (player1, p1Result, player2, p2Result) => {
    const today = new Date();
    const year = today.getFullYear();
    const month = (today.getMonth() + 1).toString().padStart(2, '0');
    const day = today.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;
    const is_pong = game === 'pong' ? true : false;

    const jsonData = {
      p1ID: player1.id,
      p1Name: player1.username,
      p1Result: p1Result,
      p2ID: player2.id,
      p2Name: player2.username,
      p2Result: p2Result,
      date: formattedDate,
      is_pong: is_pong,
    }

      fetch(backendHost + '/tournament/add_match_to_historic/', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(jsonData)
      })
      .then(response => {
        if (!response.ok) {
          throw response.error;
        }
      })
      .catch(error => {console.error('There was a problem with the fetch operation:', error);});
  }

  const handleGameEnd = (player1, p1Result, player2, p2Result) => {
    let loser;
    if (p1Result < p2Result) {
        loser = player1;
    } else {
      loser = player2;
    }

    const updatedParticipants = participants.filter(participant => participant !== loser);
    setParticipants(updatedParticipants);
    setUsers(updatedParticipants);

    fetchMatchResult(player1, p1Result, player2, p2Result);

    setCurrentMatch(null);
  };

  return (
    <div>
      {currentMatch && game == 'pong' && (
        <ThreejsGame 
        p1={currentMatch.player1} 
        p2={currentMatch.player2} 
        onGameEnd={handleGameEnd} 
        />
      )}

      {currentMatch && game == 'morpion' && (
        <Morpion 
        p1={currentMatch.player1} 
        p2={currentMatch.player2} 
        onGameEnd={handleGameEnd} 
        />

        // <>
        //    <p>Player 1: {currentMatch.player1.username}</p>
        //   <p>Player 2: {currentMatch.player2.username}</p>
        //   <button onClick={() => handleGameEnd(currentMatch.player1, 10, currentMatch.player2, 0)}>End Game (Player 1 Wins)</button>
        //   <button onClick={() => handleGameEnd(currentMatch.player1, 0, currentMatch.player2, 10)}>End Game (Player 2 Wins)</button>
        // </>
      )}

      {!currentMatch && participants.length !== 1 && (
        <>
        <h2>Tournament Participants:</h2>
        <ul>
          {participants.map((user, index) => (
            <li key={index}>
              Username: {user.username}, Profile Picture: {user.profile}
              <ProfilePic filename={user.profile} online={user.is_online} />
            </li>
          ))}
        </ul>
        <button onClick={doTournament}>PLAY !</button>
        </>
      )}

      {participants.length === 1 && (
        <div>
          <h3>The winner is: {participants[0].username}</h3>
        </div>
      )}
    </div>
  );
};

export default Matchmaking;
