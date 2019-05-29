import React from 'react';
import GenericTable from '../common/GenericTable';

const keys = [
  {title: 'Name', key: 'name'},
  {title: 'Artists', key: 'artists'},
  {title: 'Length', key: 'duration'},
];

function TrackList({ tracks }) {
  return <GenericTable items={tracks} keys={keys} name="Tracks" />;
}

export default TrackList;
