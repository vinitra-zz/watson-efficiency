package com.example.danielphillips.watson911;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
import com.google.android.gms.common.GooglePlayServicesRepairableException;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.location.places.AutocompleteFilter;
import com.google.android.gms.location.places.Place;
import com.google.android.gms.location.places.ui.PlaceAutocomplete;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.tasks.OnSuccessListener;

/**
 * Created by daniel.phillips on 7/20/17.
 */


public class EmergencyInformation extends AppCompatActivity implements OnMapReadyCallback {
    private static final String TAG = "EmergencyInformation";
    private FusedLocationProviderClient mFusedLocationClient;
    private GoogleMap googleMap = null;
    private double CurrentLat = 0;
    private double CurrentLong = 0;
    private EditText LocationInput;


    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.emergency_information);
        Button SubmitEmergency = (Button)findViewById(R.id.SubmitEmergency);
        SubmitEmergency.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
            Intent WaitingOnIntent = new Intent(EmergencyInformation.this,WaitingOnEmergResponder.class);
                WaitingOnIntent.putExtra("Lat",CurrentLat);
                WaitingOnIntent.putExtra("Long",CurrentLong);
                finish();
                startActivity(WaitingOnIntent);


            }
        });
        final SupportMapFragment mapFragment =
                (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
        LocationInput = (EditText) findViewById(R.id.input_location);
        LocationInput.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    AutocompleteFilter typeFilter;
                    Intent intent =
                            new PlaceAutocomplete.IntentBuilder(PlaceAutocomplete.MODE_FULLSCREEN)
                                    .build(EmergencyInformation.this);
                    startActivityForResult(intent, 1);
                } catch (GooglePlayServicesRepairableException e) {
                    // TODO: Handle the error.
                } catch (GooglePlayServicesNotAvailableException e) {
                    // TODO: Handle the error.
                }
            }
        });
        LocationInput.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {


                return false;
            }
        });
        mFusedLocationClient = LocationServices.getFusedLocationProviderClient(this);


    }

    @Override
    public void onMapReady(final GoogleMap googleMap) {
        this.googleMap = googleMap;
        LocationManager lm = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {

        }else{
            Location location = lm.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            if(location != null ) {
                LatLng sydney = new LatLng(location.getLatitude(), location.getLongitude());
                googleMap.moveCamera(CameraUpdateFactory.newLatLngZoom(sydney, 15));
                googleMap.addMarker(new MarkerOptions()
                        .title("Sydney")
                        .snippet("The most populous city in Australia.")
                        .position(sydney));

                CurrentLat = sydney.latitude;
                CurrentLong = sydney.longitude;


            }
        }


    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == 1) {
            if (resultCode == RESULT_OK) {
                Place place = PlaceAutocomplete.getPlace(this, data);
                LocationInput.setText(place.getAddress());
                googleMap.moveCamera(CameraUpdateFactory.newLatLngZoom(place.getLatLng(), 15));
                googleMap.addMarker(new MarkerOptions()
                        .title("Selected Location")
                        .snippet("Where You Are!")
                        .position(place.getLatLng()));
                CurrentLat = place.getLatLng().latitude;
                CurrentLong = place.getLatLng().longitude;
                Log.i(TAG, "Place: " + place.getName());
                place.getLatLng();
            } else if (resultCode == PlaceAutocomplete.RESULT_ERROR) {
                Status status = PlaceAutocomplete.getStatus(this, data);
                // TODO: Handle the error.
                Log.i(TAG, status.getStatusMessage());

            } else if (resultCode == RESULT_CANCELED) {
                // The user canceled the operation.
            }
        }
    }

}
