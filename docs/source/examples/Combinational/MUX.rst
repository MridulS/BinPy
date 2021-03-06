
Example for Mux
---------------

.. code:: python

    # Imports
    from __future__ import print_function
    from BinPy.Combinational.combinational import *
.. code:: python

    # Initializing the MUX class
    
    mux = MUX(0, 1)
    
    # Put select lines
    
    mux.selectLines(0)
    
    # Output of mux
    
    print (mux.output())

.. parsed-literal::

    0


.. code:: python

    # Input changes
    
    # Input at index 1 is changed to 0
    
    mux.setInput(1, 0)
    
    # New Output of the mux
    
    print (mux.output())

.. parsed-literal::

    0


.. code:: python

    # Changing the number of inputs
    
    # No need to set the number, just change the inputs
    
    # Input must be power of 2
    
    mux.setInputs(1, 0, 0, 1)
    
    # To get the input states
    
    print (mux.getInputStates())

.. parsed-literal::

    [1, 0, 0, 1]


.. code:: python

    # New output of mux
    
    print (mux.output())

.. parsed-literal::

    1


.. code:: python

    # Using Connectors as the input lines
    
    # Take a Connector
    
    conn = Connector()
    
    # Set Output of mux to Connector conn
    
    mux.setOutput(conn)
    
    # Put this connector as the input to gate1
    
    gate1 = AND(conn, 0)
    
    # Output of the gate1
    
    print (gate1.output())

.. parsed-literal::

    0


.. code:: python

    # Changing select lines
    
    # Selects input line 2
    
    mux.selectLine(0, 1)
    
    # New output of mux
    
    print (mux.output())

.. parsed-literal::

    0


.. code:: python

    # Information about mux instance can be found by
    
    print (mux)

.. parsed-literal::

    MUX Gate; Output: 0; Inputs: [1, 0, 0, 1];

