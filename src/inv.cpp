#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
//#include <boost/stacktrace.hpp>
#include <xtensor/xmath.hpp>
#include <Eigen/LU>
#include <Eigen/Dense>

namespace py = pybind11;

using namespace pybind11::literals;
using namespace std;

Eigen::MatrixXd inv(Eigen::MatrixXd xs) {
    return xs.inverse();
}

Eigen::VectorXd lstsq(Eigen::MatrixXd A, Eigen::VectorXd b) {
    return (A.transpose() * A).ldlt().solve(A.transpose() * b);
}



PYBIND11_PLUGIN(inv) {
    pybind11::module m("code", "auto-compiled c++ extension");
    m.def("inv", &inv);
    m.def("lstsq", &lstsq);
    return m.ptr();
}