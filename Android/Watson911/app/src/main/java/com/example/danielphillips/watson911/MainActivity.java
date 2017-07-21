package com.example.danielphillips.watson911;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView UpdateInformation = (TextView) findViewById(R.id.UpdateInfo);
        Button EmergencyBtn = (Button)findViewById(R.id.emergency);
        EmergencyBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent EmergencyInformation = new Intent(MainActivity.this, EmergencyInformation.class);
                startActivity(EmergencyInformation);
            }
        });
        UpdateInformation.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent informationIntent = new Intent(MainActivity.this,Information.class);
                startActivity(informationIntent);

            }
        });


    }
}
