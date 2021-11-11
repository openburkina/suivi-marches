<template>
    <div id="map-wrap" style="height: 80vh">
        <client-only>
            <l-map :zoom=5 :center="[9.548624660911141, 7.804160193482599]">
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <l-marker :lat-lng="[8.592724737747833, 16.074241050333463]"></l-marker>
            <l-marker :lat-lng="[9.548624660911141, 7.804160193482599]"></l-marker>
            <l-marker :lat-lng="[12.125553758062672, 15.055388119977]">
            <l-description></l-description>
            </l-marker>
            </l-map>
        </client-only>
    </div>
</template>