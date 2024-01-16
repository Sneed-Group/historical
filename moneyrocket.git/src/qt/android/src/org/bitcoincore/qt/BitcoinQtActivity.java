package org.moneyrocketcore.qt;

import android.os.Bundle;
import android.system.ErrnoException;
import android.system.Os;

import org.qtproject.qt5.android.bindings.QtActivity;

import java.io.File;

public class MoneyrocketQtActivity extends QtActivity
{
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        final File moneyrocketDir = new File(getFilesDir().getAbsolutePath() + "/.moneyrocket");
        if (!moneyrocketDir.exists()) {
            moneyrocketDir.mkdir();
        }

        super.onCreate(savedInstanceState);
    }
}
