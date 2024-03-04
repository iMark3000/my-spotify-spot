
export default function ()
<select onChange={(e) => {console.log(e.target.value)}}>
  {artist 
    ? artist.map((artist) => {
        return <option key={artist.artist_id} value={artist.artist_id}>{artist.name}</option>;
        }) 
      : null}
</select>
