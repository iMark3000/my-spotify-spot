import { Artist } from "../types/Types";

export type AppProps = {
    artist: Artist;
}

export default function ArtistDetail({ artist }: AppProps) : JSX.Element {
    return <p>{artist.name}</p>;
}