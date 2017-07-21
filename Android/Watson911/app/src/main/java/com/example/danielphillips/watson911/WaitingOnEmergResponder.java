package com.example.danielphillips.watson911;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

/**
 * Created by daniel.phillips on 7/20/17.
 */

public class WaitingOnEmergResponder extends AppCompatActivity implements OnMapReadyCallback {

    private double currentlat = 0;
    private double currentlong = 0;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.waitingonemergres);
        final ImageView AddNotes = (ImageView) findViewById(R.id.AddNotes);
        Button EndEmergency = (Button)findViewById(R.id.end_emergency);
        EndEmergency.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });

        currentlat  = getIntent().getDoubleExtra("Lat",0);
        currentlong  = getIntent().getDoubleExtra("Long",0);

        final SupportMapFragment mapFragment =
                (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map_wait);
        mapFragment.getMapAsync(this);
        AddNotes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent AddNotesIntent = new Intent(WaitingOnEmergResponder.this,AddNotes.class);
                startActivity(AddNotesIntent);
            }
        });
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        googleMap.moveCamera(CameraUpdateFactory.newLatLngZoom(new LatLng(currentlat,currentlong), 15));
        googleMap.addMarker(new MarkerOptions()
                .title("Selected Location")
                .snippet("Where You Are!")
                .position(new LatLng(currentlat,currentlong)));

    }
}
