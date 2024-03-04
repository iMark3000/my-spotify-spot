import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";
import ArtistDetail from "./components/ArtistDetail"
import { Artist } from "./types/Types"

function App() {
  const [artist, setArtist] = useState<Artist[] | null>();
  useEffect(() => {
    const url = 
    "http://localhost:8000/api/artists/";
  axios.get(url).then((response) => {
    setArtist(response.data);
  });
}, []);
  return ( 
    <div className="App">
    </div>
  );
}


export default App;
